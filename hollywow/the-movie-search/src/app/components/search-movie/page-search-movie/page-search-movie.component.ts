import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-page-search-movie',
  templateUrl: './page-search-movie.component.html',
  styleUrls: ['./page-search-movie.component.scss']
})
export class PageSearchMovieComponent implements OnInit {

  movieName: string;

  constructor() { 
    this.movieName = "";
  }

  ngOnInit(): void {
  }

  onSubmit() {
    alert("Su pelicula se llama " + this.movieName); 
  }
  
  
}
