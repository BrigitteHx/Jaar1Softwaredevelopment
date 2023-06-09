function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
  }
  
  const animalCards = ['cat','chicken','cow','dog','donkey','goat','horse','pig','rabbit','sheep'];
  let firstCard, secondCard;
  let flippedCardRow1 = null;
  let flippedCardRow2 = null;
  
  const buttonsContainer = document.getElementById('buttons');
  const firstCards = document.createElement('div');
  const secondCards = document.createElement('div');
  
  shuffle(animalCards).forEach((animal) => {
    const button = document.createElement('button');
    button.id = animal;
    const image = document.createElement('img');
    image.src = 'images/background.png';
  
    button.addEventListener('click', function () {
      if (flippedCardRow1 === button || flippedCardRow2 === button) {
        // als al goed is, niets doen
        return;
      }
  
      image.src = `images/${animal}.png`;
  
      if (flippedCardRow1 === null) {
        flippedCardRow1 = button;
        return;
      }
  
      flippedCardRow2 = button;
  
      if (flippedCardRow1 !== null && flippedCardRow2 !== null) {
        if (flippedCardRow1.id === flippedCardRow2.id) {
          // kaarten niet terug want goed
          flippedCardRow1 = null;
          flippedCardRow2 = null;
        } else {
          // kaarten terug omdraaien
          setTimeout(() => {
            flippedCardRow1.querySelector('img').src = 'images/background.png';
            flippedCardRow2.querySelector('img').src = 'images/background.png';
            flippedCardRow1 = null;
            flippedCardRow2 = null;
          }, 1000);
        }
      }
    });
  
    button.appendChild(image);
    firstCards.appendChild(button);
  });
  
  shuffle([...animalCards]).forEach((animal) => {
    const button = document.createElement('button');
    button.id = animal;
    const image = document.createElement('img');
    image.src = 'images/background.png';
  
    button.addEventListener('click', function () {
      if (flippedCardRow1 === button || flippedCardRow2 === button) {
        // als al goed is, niets doen
        return;
      }
  
      image.src = `images/${animal}.png`;
  
      if (flippedCardRow1 === null) {
        flippedCardRow1 = button;
        return;
      }
  
      flippedCardRow2 = button;
  
      if (flippedCardRow1 !== null && flippedCardRow2 !== null) {
        if (flippedCardRow1.id === flippedCardRow2.id) {
          // kaarten niet terug want goed
          flippedCardRow1 = null;
          flippedCardRow2 = null;
        } else {
          // kaarten terug omdraaien
          setTimeout(() => {
            flippedCardRow1.querySelector('img').src = 'images/background.png';
            flippedCardRow2.querySelector('img').src = 'images/background.png';
            flippedCardRow1 = null;
            flippedCardRow2 = null;
          }, 1000);
        }
      }
    });
  
    button.appendChild(image);
    secondCards.appendChild(button);
  });
  
  buttonsContainer.append(firstCards, secondCards);
  