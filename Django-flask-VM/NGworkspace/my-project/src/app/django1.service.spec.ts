import { TestBed } from '@angular/core/testing';

import { Django1Service } from './django1.service';

describe('Django1Service', () => {
  let service: Django1Service;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Django1Service);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
