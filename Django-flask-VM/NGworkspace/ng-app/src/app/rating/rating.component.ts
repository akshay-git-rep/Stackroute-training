import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrl: './rating.component.css'
})
export class RatingComponent implements OnInit{

  constructor() { }

  ngOnInit(): void {
  }

  ratingcount = 0
  totalratig = 0

  finalrating: any ;

  ratingcontrol=new FormControl(0);
  GetRating(){
    this.ratingcount++;
    this.totalratig += this.ratingcontrol?.value || 0;
    this.finalrating= (this.totalratig/this.ratingcount).toFixed(1)
    console.log(this.finalrating);
  }

}
