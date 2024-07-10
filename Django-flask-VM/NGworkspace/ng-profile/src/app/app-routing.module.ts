import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProfileComponent } from './profile/profile.component';
import { StudSubjComponent } from './stud-subj/stud-subj.component';
import { LaptopsComponent } from './laptops/laptops.component';
import { ChartsComponent } from './charts/charts.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: 'profile', component: ProfileComponent },
  { path: 'stud', component: StudSubjComponent },
  { path: 'lap', component: LaptopsComponent },
  { path: 'chart', component: ChartsComponent },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
