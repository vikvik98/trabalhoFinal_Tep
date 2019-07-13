import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FilmesComponent } from './filmes.component';

describe('FilmesComponent', () => {
  let component: FilmesComponent;
  let fixture: ComponentFixture<FilmesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FilmesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FilmesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
