import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-movie-card',
  templateUrl: './movie-card.component.html',
  styleUrls: ['./movie-card.component.scss']
})
export class MovieCardComponent implements OnInit {

  @Input() imgUrl: string;
  @Input() title: string;
  @Input() releaseDate: string;
  @Input() overview: string;

  constructor() { 
    this.imgUrl = "";
    this.title = "";
    this.releaseDate = "";
    this.overview = "";
  }

  ngOnInit(): void {
  }

}
