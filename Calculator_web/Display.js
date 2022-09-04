class Display {
    constructor(displayValAnterior, displayValActual) {
        this.displayValctual = displayValActual;
        this.displayValAnterior = displayValAnterior;
        this.calculador = new Calculadora();
        this.tipoOperacion = undefined;
        this.valActual = '';
        this.valAnterior = '';
        this.signos = {
            sumar: '+',
            dividir: '%',
            multiplicar: 'x',
            restar: '-', 
        }
    }

    borrar() {
        this.valActual = this.valActual.toString().slice(0,-1);
        this.imprimirValores();
    }

    borrarTodo() {
        this.valActual = '';
        this.valAnterior = '';
        this.tipoOperacion = undefined;
        this.imprimirValores();
    }

    computar(tipo) {
        this.tipoOperacion !== 'igual' && this.calcular();
        this.tipoOperacion = tipo;
        this.valAnterior = this.valActual || this.valAnterior;
        this.valActual = '';
        this.imprimirValores();
    }

    agregarNumero(numero) {
        if(numero === '.' && this.valActual.includes('.')) return
        this.valActual = this.valActual.toString() + numero.toString();
        this.imprimirValores();
    }

    imprimirValores() {
        this.displayValActual.textContent = this.valActual;
        this.displayValAnterior.textContent = `${this.valAnterior} ${this.signos[this.tipoOperacion] || ''}`;
    }

    calcular() {
        const valAnterior = parseFloat(this.valAnterior);
        const valActual = parseFloat(this.valActual);

        if( isNaN(valActual)  || isNaN(valAnterior) ) return
        this.valActual = this.calculador[this.tipoOperacion](valAnterior, valActual);
    }
}
