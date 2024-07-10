import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Django1Component } from './django1/django1.component';
import { NewsComponent } from './news/news.component';
import { EmpsComponent } from './emps/emps.component';
import { StudentsComponent } from './students/students.component';
import { ProfileComponent } from './profile/profile.component';

@NgModule({
  declarations: [
    AppComponent,
    Django1Component,
    NewsComponent,
    EmpsComponent,
    StudentsComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
