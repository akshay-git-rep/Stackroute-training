export class Lap {
    id: number = 0;
    model: string = '';
    price: number = 0;
    company: string = '';
constructor(id: number, model: string, price:number, company:string) {
        this.id = id;
        this.model = model;
        this.price = price;
        this.company = company;
    }
}