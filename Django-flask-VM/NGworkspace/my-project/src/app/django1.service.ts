import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class Django1Service {
  _url: string = "http://127.0.0.1:8000/api/bookvs/";
  

  constructor() { }

  getdata() {
    return fetch(this._url).then((res) => res.json());
  };
}
