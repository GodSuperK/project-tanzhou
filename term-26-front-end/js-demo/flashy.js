// 定时器： 每隔一段时间执行一次动作
// setInterval("执行代码", 间隔时间)单位毫秒
// setInterval("alert(1);", 2000);
// 查找元素
var div_flashy = document.getElementById('flashy');
function run_flashy() {
  // 获取文本节点
  var text = div_flashy.innerText;
  // 字符串处理,并重新为文本节点赋值
  div_flashy.innerText = text.substring(1,text.length)+text.charAt(0);
}
// 创建定时器去执行该操作
setInterval("run_flashy();", 1000);
