import { WEBSITE_NAME } from "../BLOG_CONSTANTS/_BLOG_SETUP"

const Footer = () => {
    const year = new Date().getFullYear()

    return (
        <div className={"dark:bg-slate-900 dark:text-white bg-slate-100 text-black"}>
            <div className="md:container flex items-center md:justify-center justify-around flex-wrap md:text-[14px] text-[12px] py-5">
                <p className="my-0 mr-[10px] md:mr-3">SIH1330 - {WEBSITE_NAME} - {year}</p>
            </div>
        </div>
    )
}

export default Footer