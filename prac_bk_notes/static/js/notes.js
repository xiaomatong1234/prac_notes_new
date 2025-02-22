// static/js/scripts.js
window.onload = function() {
    document.body.addEventListener('click', function() {
        window.location.href = "/notes"; // 使用蓝图的 URL，或者动态的生成 URL
    });
};
//点击首页任何地方都能跳转