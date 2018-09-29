# coding: utf-8

__author__ = 'lau.wenbo'

"""
CNN卷积算法识别验证码
"""
import tensorflow as tf
from captcha.image import  ImageCaptcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import  Image
import random

number=['0','1','2','3','4','5','6','7','8','9']
#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def random_captcha_text(char_set=number,captcha_size=4):
    captcha_text=[]
    for i in range(captcha_size):
        c=random.choice(char_set)
        captcha_text.append(c)
    return captcha_text

def gen_captcha_text_image():
    image=ImageCaptcha()
    captcha_text=random_captcha_text()
    captcha_text=''.join(captcha_text)
    captcha=image.generate(captcha_text)
    captcha_image=Image.open(captcha)
    captcha_image=np.array(captcha_image)
    return captcha_text,captcha_image


def convert2gray(img):
    if len(img.shape)>2:
        r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img


def text2vec(text):
    text_len = len(text)
    if text_len > max_captcha:
        raise ValueError('验证码最长4个字符')

    vector = np.zeros(max_captcha * char_set_len)

    def char2pos(c):
        if c == '_':
            k = 62
            return k
        k = ord(c) - 48
        if k > 9:
            k = ord(c) - 55
            if k > 35:
                k = ord(c) - 61
                if k > 61:
                    raise ValueError('No Map')
        return k

    for i, c in enumerate(text):
        idx = i * char_set_len + char2pos(c)
        vector[idx] = 1
    return vector


def get_next_batch(batch_size=128):
    batch_x=np.zeros([batch_size,image_height*image_width])
    batch_y=np.zeros([batch_size,max_captcha*char_set_len])

    def wrap_gen_captcha_text_and_image():
        while True:
            text, image = gen_captcha_text_image()
            if image.shape == (60, 160, 3):
                return text, image

    for i in range(batch_size):
        text, image = wrap_gen_captcha_text_and_image()
        image = convert2gray(image)

        batch_x[i, :] = image.flatten() / 255
        batch_y[i, :] = text2vec(text)

    return batch_x, batch_y

def cnn_structure(w_alpha=0.01, b_alpha=0.1):
    x = tf.reshape(X, shape=[-1, image_height, image_width, 1])


    wc1=tf.get_variable(name='wc1',shape=[3,3,1,32],dtype=tf.float32,initializer=tf.contrib.layers.xavier_initializer())
    #wc1 = tf.Variable(w_alpha * tf.random_normal([3, 3, 1, 32]))
    bc1 = tf.Variable(b_alpha * tf.random_normal([32]))
    conv1 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(x, wc1, strides=[1, 1, 1, 1], padding='SAME'), bc1))
    conv1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    conv1 = tf.nn.dropout(conv1, keep_prob)

    wc2=tf.get_variable(name='wc2',shape=[3,3,32,64],dtype=tf.float32,initializer=tf.contrib.layers.xavier_initializer())
   # wc2 = tf.Variable(w_alpha * tf.random_normal([3, 3, 32, 64]))
    bc2 = tf.Variable(b_alpha * tf.random_normal([64]))
    conv2 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv1, wc2, strides=[1, 1, 1, 1], padding='SAME'), bc2))
    conv2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    conv2 = tf.nn.dropout(conv2, keep_prob)

    wc3=tf.get_variable(name='wc3',shape=[3,3,64,128],dtype=tf.float32,initializer=tf.contrib.layers.xavier_initializer())
    #wc3 = tf.Variable(w_alpha * tf.random_normal([3, 3, 64, 128]))
    bc3 = tf.Variable(b_alpha * tf.random_normal([128]))
    conv3 = tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(conv2, wc3, strides=[1, 1, 1, 1], padding='SAME'), bc3))
    conv3 = tf.nn.max_pool(conv3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    conv3 = tf.nn.dropout(conv3, keep_prob)


    wd1=tf.get_variable(name='wd1',shape=[8*20*128,1024],dtype=tf.float32,initializer=tf.contrib.layers.xavier_initializer())
    #wd1 = tf.Variable(w_alpha * tf.random_normal([7*20*128,1024]))
    bd1 = tf.Variable(b_alpha * tf.random_normal([1024]))
    dense = tf.reshape(conv3, [-1, wd1.get_shape().as_list()[0]])
    dense = tf.nn.relu(tf.add(tf.matmul(dense, wd1), bd1))
    dense = tf.nn.dropout(dense, keep_prob)

    wout=tf.get_variable('name',shape=[1024,max_captcha * char_set_len],dtype=tf.float32,initializer=tf.contrib.layers.xavier_initializer())
    #wout = tf.Variable(w_alpha * tf.random_normal([1024, max_captcha * char_set_len]))
    bout = tf.Variable(b_alpha * tf.random_normal([max_captcha * char_set_len]))
    out = tf.add(tf.matmul(dense, wout), bout)
    return out

def train_cnn():
    output=cnn_structure()
    cost=tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=output,labels=Y))
    optimizer=tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
    predict=tf.reshape(output,[-1,max_captcha,char_set_len])
    max_idx_p = tf.argmax(predict, 2)
    max_idx_l = tf.argmax(tf.reshape(Y, [-1, max_captcha, char_set_len]), 2)
    correct_pred = tf.equal(max_idx_p, max_idx_l)
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    saver=tf.train.Saver()

    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        step = 0
        while True:
            batch_x, batch_y = get_next_batch(100)
            _, cost_= sess.run([optimizer, cost], feed_dict={X: batch_x, Y: batch_y, keep_prob: 0.75})
            print(step, cost_)
            if step % 10 == 0:
                batch_x_test, batch_y_test = get_next_batch(100)
                acc = sess.run(accuracy, feed_dict={X: batch_x_test, Y: batch_y_test, keep_prob: 1.})
                print(step, acc)
                if acc > 0.99:
                    saver.save(sess, "./model/crack_capcha.model", global_step=step)
                    break
            step += 1


def crack_captcha(captcha_image):
    output = cnn_structure()

    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, "./model/crack_capcha.model-1200")

        predict = tf.argmax(tf.reshape(output, [-1, max_captcha, char_set_len]), 2)
        text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1.})
        text = text_list[0].tolist()
        return text

if __name__=='__main__':
    train=1
    if train==0:
        text,image=gen_captcha_text_image()
        print("验证码大小：",image.shape)#(60,160,3)

        image_height=60
        image_width=160
        max_captcha=len(text)
        print("验证码文本最长字符数",max_captcha)
        char_set=number
        char_set_len=len(char_set)

        X = tf.placeholder(tf.float32, [None, image_height * image_width])
        Y = tf.placeholder(tf.float32, [None, max_captcha * char_set_len])
        keep_prob = tf.placeholder(tf.float32)
        train_cnn()

    if train == 1:
        image_height = 60
        image_width = 160
        char_set = number
        char_set_len = len(char_set)

        text, image = gen_captcha_text_image()

        f = plt.figure()
        ax = f.add_subplot(111)
        ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
        plt.imshow(image)

       # plt.show()

        max_captcha = len(text)
        image = convert2gray(image)
        image = image.flatten() / 255

        X = tf.placeholder(tf.float32, [None, image_height * image_width])
        Y = tf.placeholder(tf.float32, [None, max_captcha * char_set_len])
        keep_prob = tf.placeholder(tf.float32)

        predict_text = crack_captcha(image)
        print("正确: {}  预测: {}".format(text, predict_text))


        plt.show()
