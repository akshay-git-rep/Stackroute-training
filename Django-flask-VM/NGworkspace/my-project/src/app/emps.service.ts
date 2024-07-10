import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EmpsService {
  _url: string = "http://127.0.0.1:8000/api/empvs/";
  

  constructor() { }

  getdata() {
    return fetch(this._url).then((res) => res.json());
  };
}
