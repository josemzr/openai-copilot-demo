export class Task {
  id: string;
  name: string;
  description: string;
  done: boolean;

  constructor(id: string, name: string, description: string, done: boolean) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.done = done;
  }
}