// buttons3

function generateButtons(numButtons) {
    var container = document.createElement("div");
    container.className = "button-container";
    document.body.appendChild(container);
  
    var buttonsPerRow = 5;
  
    for (var i = 1; i <= numButtons; i++) {
      var button = document.createElement("button");
      button.className = "number-button";
      button.innerText = i;
      container.appendChild(button);
  
      button.addEventListener("click", function() {
        this.style.backgroundColor = "red"; // knop naar rood
      });
    }
  
    for (var j = 0; j < (buttonsPerRow - (numButtons % buttonsPerRow)) % buttonsPerRow; j++) {
      var emptyButton = document.createElement("button");
      emptyButton.className = "number-button empty-button";
      container.appendChild(emptyButton);
    }
  }
  
  generateButtons(30);
  