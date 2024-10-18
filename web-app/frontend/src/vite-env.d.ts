declare module "*.vue";

declare module "*.svg" {
  import { DefineComponent } from "vue";
  const component: DefineComponent<object, object, object>;
  export default component;
}
