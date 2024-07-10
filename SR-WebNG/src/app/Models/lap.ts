export class Lap {
    id : string = '';
    model : string = '';
    company : string = '';
    price : number = 0;

    constructor(id : string, model : string, company : string, price : number){
        this.id = id;
        this.model = model;
        this.company = company;
        this.price = price;
    }
}