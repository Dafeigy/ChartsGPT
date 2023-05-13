const userInput = document.getElementById("user-input");
const submitButton = document.getElementById("submit-button");
const loadingAnimation = document.getElementById("loading-animation");
const chartContainer = document.getElementById("chart-container");

// 初始化ECharts实例
const chart = echarts.init(chartContainer);
console.log("ECharts initialized.")

var textarea = document.getElementById("user-input");
textarea.style.height = textarea.scrollHeight + "px";
textarea.addEventListener("input", function() { 
    this.style.height = "auto"; 
    this.style.height = this.scrollHeight + "px"; 
});

function f(){

  $.ajax({
      url:"/json",
      type:"get",
      async: true,
      timeout: 60000,
      beforeSend:function(){document.getElementById('user-input').disabled = true},
      success:function (data) {
          document.getElementById('user-input').disabled = false
          chart.clear()
          chart.setOption(JSON.parse(data));
      },
      error:function (data) {
          alert("获取返回json失败，console已记录返回数据")
          console.log(data)
      },
      complete:function(){document.getElementById('user-input').disabled = false;}
  })

  
  }


$("#generate").click(function () {
  var Text = document.getElementById('user-input').value;
  var input = {
      'user-input': `${Text}`,
  };
  
  $.ajax({
      url: '/ajax',
      type: 'POST',
      data: JSON.stringify(input),
      dataType: "json",
      contentType: "application/json",
      success:function (d) {
          console.log("数据提交成功")
      },
      error:function (d) {
          console.log(d)
          alert("提交数据失败，请检查代理设置或余额。")
      }
  })
  
  f();
})