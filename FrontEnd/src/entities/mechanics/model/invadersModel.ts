import { Invader } from "../types/invader";

export const flagGrunt: Invader = {
  score: 250,
  health: 500,
  icon: "/assets/Sprites/bucket.webp",
  typeCode: "G1",
};

export const spearGrunt: Invader = {
  score: 500,
  health: 1000,
  icon: "/assets/Sprites/spear.webp",
  typeCode: "G2",
};

export const swordGrunt: Invader = {
  score: 1250,
  health: 2500,
  icon: "/assets/Sprites/sword.webp",
  typeCode: "G3",
};

export const musketeer: Invader = {
  score: 15000,
  health: 25000,
  icon: "/assets/Sprites/musketeer.webp",
  typeCode: "M",
};

export const warrior: Invader = {
  score: 50000,
  health: 50000,
  icon: "/assets/Sprites/warrior.webp",
  typeCode: "W",
};

export const battleMage: Invader = {
  score: 750000,
  health: 500000,
  icon: "/assets/Sprites/bannerholder0.webp",
  typeCode: "BW",
};

export const INVADERS_LIST = [
  flagGrunt,
  spearGrunt,
  swordGrunt,
  warrior,
  musketeer,
  battleMage,
];
