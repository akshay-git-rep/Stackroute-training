import { Injectable } from '@angular/core';
import { Lap } from './Models/laps';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class FavService {
  laps: Lap[] = [];
  changeCount: any;
  sum : number = 0;
  private _url: any;

  constructor(private toastr: ToastrService) { }

}
