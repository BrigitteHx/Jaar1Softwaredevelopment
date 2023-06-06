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
  
      // klik op button
      button.addEventListener("click", function() {
        // HULP STACK OVERFLOW DATA KLEUR EN DATA KLIK OPHALEN: 
        var currentColor = this.getAttribute("data-color"); 
        var currentClicks = parseInt(this.getAttribute("data-clicks")) || 0; 
  
        // kleuren
        if (currentClicks === 0) {
          this.style.backgroundColor = "red";
          this.setAttribute("data-color", "red");
        } else if (currentClicks === 1) {
          this.style.backgroundColor = "purple";
          this.setAttribute("data-color", "purple");
        } else if (currentClicks === 2) {
          this.style.backgroundColor = "blue";
          this.setAttribute("data-color", "blue");
        } else if (currentClicks === 3) {
          this.style.backgroundColor = "black";
          this.setAttribute("data-color", "black");
        }
  
        currentClicks++; 
  
        // is kleur zwart?
        if (currentClicks === 5 && currentColor === "black") {
          this.remove(); // remove uit DOM
        } else {
          this.setAttribute("data-clicks", currentClicks); 
        }
      });
    }
  
    for (var j = 0; j < (buttonsPerRow - (numButtons % buttonsPerRow)) % buttonsPerRow; j++) {
      var emptyButton = document.createElement("button");
      emptyButton.className = "number-button empty-button";
      container.appendChild(emptyButton);
    }
  }
  
  generateButtons(30);
  