import { LogoType, NavbarType } from "./enums";

export interface IAuthor {
  profilePic?: string;
  name: string;
  designation?: string;
  bio?: string;
  social?: iNavSocials[];
}

export interface iArticle {
  id : string;
  featureArticle?: boolean;
  author: IAuthor;
  date: string;
  articleTitle: string;
  tags: string[];
  thumbnail?: string;
  shortIntro: string;
  content: any;
  category?: string;
}

export interface iNavbar {
  toggleSideMenu: () => void;
  changeTheme?: () => void;
  navSetup: iNavSetup;
}

export interface iNavSetup {
  type: NavbarType,
  navLinks: iNavLink[];
  sideNavLinks: iNavLink[];
  logo: iNavLogo;
}

export interface iNavLogo {
  type: LogoType;
  logo: string;
  logoLight?: string;
}

export interface iNavLink {
  label: string;
  path: string;
  type?: string;
  newTab?: boolean;
  link? : string;
}

export interface iNavSocials {
  link: string;
  icon: any;
}
