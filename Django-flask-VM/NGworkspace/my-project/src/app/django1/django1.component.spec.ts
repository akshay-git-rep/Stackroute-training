import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Django1Component } from './django1.component';

describe('Django1Component', () => {
  let component: Django1Component;
  let fixture: ComponentFixture<Django1Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [Django1Component]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(Django1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
