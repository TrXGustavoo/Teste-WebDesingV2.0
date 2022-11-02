function Calcular() {
    let inputNome = document.getElementById('inputNome')
    let inputAltura = document.getElementById('inputAlt')
    let inputPeso = document.getElementById('inputPeso')

    let res = document.getElementById('res')
    res.innerHTML = ''

    let VinputNome = inputNome.value
    let VinputAlt = Number(inputAltura.value)
    let VinputPeso = Number(inputPeso.value)

    const resultado = VinputPeso / (VinputAlt * VinputAlt)

    console.log(resultado)

    if (resultado < 18.5) {
        res.innerHTML += `${VinputNome} seu IMC é de ${Math.floor(resultado)} e você está abaixo do peso`
    } else if (resultado >= 18.5 && resultado < 25) {
        res.innerHTML += `${VinputNome} seu IMC é de ${Math.floor(resultado)} e você está com o peso ideal parabens!!!`
    } else if (resultado >= 25 && resultado < 30) {
        res.innerHTML += `${VinputNome} seu IMC é de ${Math.floor(resultado)} e você está levemente acima do peso`
    } else if (resultado >= 30 && resultado < 40) {
        res.innerHTML += `${VinputNome} seu IMC é de ${Math.floor(resultado)} e você está com o obesidade grau II cuidado!!!`
    } else if (resultado >= 40) {
        res.innerHTML += `${VinputNome} seu IMC é de ${Math.floor(resultado)} e você está com o obesidade grau III cuidado!!!`
    }
    else {
        console.log('erro')
    }

}
