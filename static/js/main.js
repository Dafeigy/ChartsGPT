const userInput = document.getElementById("user-input");
const submitButton = document.getElementById("submit-button");
const loadingAnimation = document.getElementById("loading-animation");
const chartContainer = document.getElementById("chart-container");

// 初始化ECharts实例
const chart = echarts.init(chartContainer);
console.log("ECharts initialized.")

// 为表单添加事件监听器
document.getElementById("chart-form").addEventListener("submit", async (event) => {
  event.preventDefault();
    console.log("hello")
  userInput.disabled = true;
  submitButton.disabled = true;
  loadingAnimation.style.display = "block";
});