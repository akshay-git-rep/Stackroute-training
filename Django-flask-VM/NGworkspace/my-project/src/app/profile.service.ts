import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  _url: string = "http://127.0.0.1:8000/api/profilevs/";
  _url1: string = "http://127.0.0.1:8000/api/feedvs/";

  constructor() { }

  getprodata() {
    return fetch(this._url).then((res) => res.json());
  };
  getfeeddata() {
    return fetch(this._url1).then((res) => res.json());
  };
}
