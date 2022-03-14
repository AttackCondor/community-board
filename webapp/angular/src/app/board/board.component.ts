import { Component, OnInit, } from '@angular/core';
import * as Color from 'color';
import { rgb } from 'color';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {

  pixelButtons!: any[];
  selectedColor: string = "white";
  
  constructor() { }

  ngOnInit(): void {
    this.pixelButtons = new Array(2048).fill("black");
  }

  clickPixel(idx: number) {
    this.pixelButtons.splice(idx, 1, this.selectedColor);
  }

  clearScreen(){
    this.pixelButtons.fill("black");
  }

  setSelectedColor(color: string){
    this.selectedColor = color;
  }

}
