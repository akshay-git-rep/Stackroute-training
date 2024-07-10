import { Component, OnInit } from '@angular/core';
import { EmpsService } from '../emps.service';

@Component({
  selector: 'app-emps',
  templateUrl: './emps.component.html',
  styleUrl: './emps.component.css'
})
export class EmpsComponent implements OnInit {
  empsdata: any;

  constructor(private empsService: EmpsService) { }

  ngOnInit(){
    this.empsService.getdata().then((data) => {
      this.empsdata = data;
      console.log(data);
    }).catch((err) => {
      console.log(err);
    });
  }

  splitProjects(item: any) {
    // console.log(e);
    return item.project.split(',');
  }
}