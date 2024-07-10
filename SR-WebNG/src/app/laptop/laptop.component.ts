import { Component, OnInit } from '@angular/core';
import { LaptopService } from '../laptop.service';
import { FormBuilder } from '@angular/forms';
import { Lap } from '../Models/lap';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-laptop',
  templateUrl: './laptop.component.html',
  styleUrl: './laptop.component.css'
})
export class LaptopComponent implements OnInit{
  laptops : any;
  start : boolean = true;
  markCount  = 0;
  markedLaptops = new Set();
  error : string = "";

  constructor(private laptopService: LaptopService, private fb : FormBuilder, private toastr: ToastrService) {}

  ngOnInit(){
    this.getLaptopFromService();
  }

  lapForm = this.fb.group({
    id : [''],
    model : [''],
    company : [''],
    price : [''],
  })

  onSubmit() {
    let id = (this.lapForm.value.id) || "";
    let model = this.lapForm.value.model || "";
    let company = this.lapForm.value.company || "";
    let price = Number(this.lapForm.value.price);

    console.log("ID : ", id,"model : ", model, "price : ", price, "company : ", company);
    this.addLaptop(new Lap(id, model, company, price))
    this.lapForm.reset();
  }

  addLaptop(lap: Lap) {
    this.laptopService.addLaptop(lap).then(() => {
      this.getLaptopFromService();
    })
    this.toastr.success('Laptop added successfully');
  }

  deleteLaptop(lapId: string) {
    // console.log("delete initated")
    this.laptopService.deleteLaptop(lapId).then(() => {
      if (this.markedLaptops.has(lapId)) {
        this.markedLaptops.delete(lapId); 
        this.markCount--;
      }
      this.getLaptopFromService();
    })
    this.toastr.error('Laptop deleted successfully');
  }

  markLaptop(lapId: string) {
    if (this.markedLaptops.has(lapId)) {
      this.markedLaptops.delete(lapId); 
      this.markCount--;
      this.toastr.success('Laptop un-marked successfully');
    } else {
      this.markedLaptops.add(lapId); 
      this.markCount++;
      this.toastr.success('Laptop marked successfully');
    }
  }
  getLaptopFromService() {
    this.laptopService.getLaptops().then((data) => {
      console.log(data);
      this.laptops = data;
    }).catch((err) => {
      console.log(err);
      this.error = 'ERROR while fetching';
    });
  }
  }

