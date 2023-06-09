function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
  }
  
  const animalCards = ['cat','chicken','cow','dog','donkey','goat','horse','pig','rabbit','sheep'];
  let firstCard, secondCard;
  
  const buttonsContainer = document.getElementById('buttons');
  const firstCards = document.createElement('div');
  const secondCards = document.createElement('div');
  
  shuffle(animalCards).forEach((animal) => {
    const button = document.createElement('button');
    button.id = animal;
    const image = document.createElement('img');
    image.src = 'images/background.png';
  
    button.addEventListener('click', function () {
      image.src = `images/${animal}.png`;
      firstCard = button.id;
    //   console.log(firstCard);
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
      image.src = `images/${animal}.png`;
      secondCard = button.id;
    });
  
    button.appendChild(image);
    secondCards.appendChild(button);
  });
  
  buttonsContainer.append(firstCards, secondCards);  

// button.innerText = animal;