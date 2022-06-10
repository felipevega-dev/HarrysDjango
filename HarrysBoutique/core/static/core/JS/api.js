async function start(){
    const response = await fetch("https://dog.ceo/api/breeds/list/all")
    const data = await response.json()
    createBreedList(data.message)

}

start()


function createBreedList(breedList){
    document.getElementById('breed').innerHTML =
    `
    <select onchange="loadByBreed(this.value)">
      <option>Elija una raza de perro</option>
      ${Object.keys(breedList).map(function (breed){
        return `<option>${breed}</option>`
       }).join('')}
    </select>
    `
}


async function loadByBreed(breed){
  if (breed !="choose a dog breed"){
    const response = await fetch(`https://dog.ceo/api/breed/${breed}/images`)
    const data = await response.json()
    obtenerycambiar(data.message)
  }
}

function obtenerycambiar(images){
  document.getElementById('slideshow').innerHTML=
  `
  <div class="slidedog" style="background-image: url('${images[0]}')"></div>
  `
}