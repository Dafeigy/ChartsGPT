const userInput = document.getElementById("user-input");
const submitButton = document.getElementById("submit-button");
const loadingAnimation = document.getElementById("loading-animation");
const chartContainer = document.getElementById("chart-container");

// 初始化ECharts实例
const chart = echarts.init(chartContainer);
console.log("ECharts initialized.")


// 自适应Textarea缩放
var textarea = document.getElementById("user-input");
textarea.style.height = textarea.scrollHeight + "px";
textarea.addEventListener("input", function() { 
    this.style.height = "auto"; 
    this.style.height = this.scrollHeight + "px"; 
});
const optool = {"toolbox": {
  "show": true,
  "x": 'center',
  "y": 'bottom',  
  "feature": {
      "dataView": { show: true, readOnly: false },
      "saveAsImage": {show: true, title: '保存截图', type: 'png'}}},}

function checkBalance(){
    document.getElementById("refresh").disabled = true
    console.log("Checking balance")
    $.ajax({
        url:"/balance",
        type:"get",
        async: true,
        timeout: 5000,
        success:function (data) {
            document.getElementById('balance').value = `${data} p`
            document.getElementById("refresh").disabled = false
            console.log(`${data} p remains.`)
        },
        error:function (data) {
            alert("获取点数失败，请检查token设置")
            document.getElementById('balance').value = `-0 p`
            document.getElementById("refresh").disabled = false
        },
    })
}

// checkBalance()

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
  
  $.ajax({
      url:"/json",
      type:"get",
      async: true,
      timeout: 60000,
      beforeSend:function(){
        document.getElementById('user-input').disabled = true
        document.getElementById('generate').disabled = true
        document.getElementById('loader').style.display = 'flex'
    },
      success:function (data) {
        data = data.replace("```json","")
        data = data.replace("```",'')
          document.getElementById('user-input').disabled = false
          document.getElementById('generate').disabled = false
          document.getElementById('loader').style.display = 'none'
          chart.clear()
          chart.setOption(optool)
          chart.setOption($.parseJSON(data));
      },
      error:function (data) {
          alert("获取返回json失败，console已记录返回数据")
          console.log(data)
      },
      complete:function(){
        document.getElementById('user-input').disabled = false
        document.getElementById('generate').disabled = false
        document.getElementById('loader').style.display = 'none'
      }
  })
})

$("#refresh").click(function(){
    checkBalance()
})

// setInterval(checkBalance, 30000) #定时查看