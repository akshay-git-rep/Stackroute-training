import { Injectable } from '@angular/core';
import { Lap } from './Models/laps';

@Injectable({
  providedIn: 'root'
})
export class ComputerService {
  _url: string = 'http://localhost:3000/laps';

  constructor() { }

  addLaptop(lap: any) {
    return fetch(this._url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(lap),
    })
  }

  deleteLaptop(lapId: string) {
    return fetch(`${this._url}/${lapId}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
    })
  }

  getLaptops() {
    return fetch(this._url).then((res) => res.json());
  }

  getLaptopById(id: string) {
    return fetch(this._url + id).then((res) => res.json());
  }
}
