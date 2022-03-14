import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-pixel-button',
  styleUrls: ['./pixel-button.component.css'],
  template: `
    <button class="buttonBlack" *ngIf="value=='black'"></button>
    <button class="buttonWhite" *ngIf="value=='white'"></button>
    <button class="buttonBlue" *ngIf="value=='blue'"></button>
    <button class="buttonGreen" *ngIf="value=='green'"></button>
    <button class="buttonYellow" *ngIf="value=='yellow'"></button>
  `
})

export class PixelButtonComponent {

  @Input() value!: "black" | "white" | "blue" | "green" | "yellow";
  
}
