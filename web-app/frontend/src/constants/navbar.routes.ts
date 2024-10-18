import { LockClosedIcon, HomeIcon } from "@heroicons/vue/24/outline";
import { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";

type Item = {
  name: string;
  icon: FunctionalComponent<HTMLAttributes & VNodeProps, Record<string, never>>;
  path?: string;
  url?: string;
  description: string;
  comingSoon?: boolean;
};

type Routes = {
  title: string;
  path?: string;
  icon: FunctionalComponent<HTMLAttributes & VNodeProps, Record<string, never>>;
  menuOptions: {
    footer: never[];
    items: Item[];
  };
};

export const navbarRoutes = [
  {
    title: "Home",
    icon: HomeIcon,
    path: "/",
  },
  {
    title: "Login",
    icon: LockClosedIcon,
    path: "/login",
  },
] as Routes[];
