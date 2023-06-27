document.addEventListener('DOMContentLoaded', function() {
    var messageElement = document.getElementById('message');
    
    messageElement.addEventListener('click', function() {
      var backgroundPage = chrome.extension.getBackgroundPage();
      backgroundPage.displayPopupMessage('Clicked!');
    });
  });
  