import { Component, OnInit } from '@angular/core';
import { ThemoviedbService } from '../../../services/themoviedb.service';
import { CommonModule } from '@angular/common';

export interface MovieInterface {
  adult: boolean;
  backdrop_path: string;
  genre_ids: number[];
  id: number;
  original_language: string;
  original_title: string;
  overview: string;
  popularity: number;
  poster_path: string;
  release_date: string;
  title: string;
  video: boolean;
  vote_average: number;
  vote_count: number;
}

@Component({
  selector: 'app-page-search-movie',
  templateUrl: './page-search-movie.component.html',
  styleUrls: ['./page-search-movie.component.scss']
})
export class PageSearchMovieComponent implements OnInit {

  movieName: string;
  moviesList: MovieInterface[];

  constructor(private themoviedbService: ThemoviedbService) {
    this.movieName = "";
    this.moviesList = [];
  }

  ngOnInit(): void {
  }

  onSubmit() {
    //alert("Su pelicula se llama " + this.movieName); 

    this.themoviedbService.getMovies(this.movieName)
      .subscribe(
        (data) => {
          console.log(data.results);
          this.moviesList = data.results;
        }
      );

    //console.log(this.themoviedbService.getMovies(this.movieName));
  }


}
