export class Data {
    id : number = 0;
    title : string = '';
    author : string = '';


    constructor(id : number, title : string, author : string){
        this.id = id;
        this.title = title;
        this.author = author;
    }
}