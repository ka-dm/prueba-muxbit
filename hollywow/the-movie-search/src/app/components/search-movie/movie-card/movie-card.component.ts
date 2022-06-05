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

  constructor() { 
    this.imgUrl = "";
    this.title = "";
    this.releaseDate = "";
  }

  ngOnInit(): void {
  }

}
