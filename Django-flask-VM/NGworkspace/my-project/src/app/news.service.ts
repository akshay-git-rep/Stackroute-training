import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  _url: string = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=4e59ebbc0ef04a478c43843eaa91943c';


  constructor() { }
  
  getNews() {
    return fetch(this._url).then((res) => res.json());
  }
}

