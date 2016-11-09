$(function() { (function() {
    var curr = 0;
    $("#jsNav .trigger").each(function(i) {
      $(this).click(function() {
        curr = i;
        $("#js img").eq(i).fadeIn("slow").siblings("img").hide();
        $(this).siblings(".trigger").removeClass("imgSelected").end().addClass("imgSelected");
        return false;
      });
    });

    var pg = function(flag) {
      //flag:true表示前翻， false表示后翻
      if (flag) {
        if (curr == 0) {
          todo = 2;
        } else {
          todo = (curr - 1) % 5;
        }
      } else {
        todo = (curr + 1) % 5;
      }
      $("#jsNav .trigger").eq(todo).click();
    };

    //前翻
    $("#prev").click(function() {
      pg(true);
      return false;
    });

    //后翻
    $("#next").click(function() {
      pg(false);
      return false;
    });

    //自动翻
    var timer = setInterval(function() {
      todo = (curr + 1) % 5;
      $("#jsNav .trigger").eq(todo).click();
    },
    4000);

    //鼠标悬停在触发器上时停止自动翻
    $("#jsNav a").hover(function() {
      clearInterval(timer);
    },
    function() {
      timer = setInterval(function() {
        todo = (curr + 1) % 5;
        $("#jsNav .trigger").eq(todo).click();
      },
      1500);
    });
  })();
});