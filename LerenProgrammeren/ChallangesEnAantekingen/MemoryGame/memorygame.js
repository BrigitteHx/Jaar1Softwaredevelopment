// memory game JS

let imageLijst = ['imagecat', 'imagechicken', 'imagecow', 'imagedog', 'iimagedonkey', 'imagegoat', 'imagehorse', 'imagepig', 'imagerabbit', 'imagesheep'];
imageLijst = shuffle(imageLijst);

// shuffelen 
function shuffle(array) {
  let currentIndex = array.length, randomIndex;

  while (currentIndex != 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
  }

  return array;
}

// plaatjes
function addImages() {
  const images = document.getElementById('images');

  for (let i = 0; i < imageLijst.length; i++) {
    const image = document.createElement('img');

  }
}

// function startGame() {
//   addImages();
// }

