import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent implements OnInit{
  profiledata: any;
  feeddata: any;

  constructor(private profileService: ProfileService) { }

  ngOnInit(): void {
    this.profileService.getprodata().then((data) => {
      this.profiledata = data;
      console.log(data);
    }).catch((err) => {
      console.log(err);
    });
    this.profileService.getfeeddata().then((data) => {
      this.feeddata = data;
      console.log(data);
    }).catch((err) => {
      console.log(err);
    });
  }
  
}
