import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PageSearchMovieComponent } from './page-search-movie.component';

describe('PageSearchMovieComponent', () => {
  let component: PageSearchMovieComponent;
  let fixture: ComponentFixture<PageSearchMovieComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PageSearchMovieComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PageSearchMovieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
