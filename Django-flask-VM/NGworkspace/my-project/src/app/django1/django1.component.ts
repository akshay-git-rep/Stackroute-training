import { Component, OnInit } from '@angular/core';
import { Django1Service } from '../django1.service';

@Component({
  selector: 'app-django1',
  templateUrl: './django1.component.html',
  styleUrl: './django1.component.css'
})
export class Django1Component implements OnInit {
  djdata: any;

  constructor(private django1Service: Django1Service) { }

  ngOnInit(){
    this.django1Service.getdata().then((data) => {
      this.djdata = data;
      console.log(data);
    // }).catch((err) => {
    //   console.log(err);
    });
  }
}
