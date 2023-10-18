import { SORTED_ARTICLES_BY_DATE } from "../BLOG_CONSTANTS/_ARTICLES_LIST"
import useMainContext from "../context/MainContext"
import { iArticle } from "../shared/interfaces"
import Seperator from "./Seperator"
import Text from "./Text/Text"
import { useRouter } from "next/navigation"

const FeaturedArticleSection = () => {

    const { setSelectedArtical } : any = useMainContext();
    // const featureArticles = SORTED_ARTICLES_BY_DATE.filter((article: iArticle) => article.featureArticle === true)
    const featureArticles = SORTED_ARTICLES_BY_DATE.filter((article: iArticle) => true) // take all articles

    const router = useRouter();

    return (

        featureArticles.length ?
            (<>
                <Text subtitle className="mb-5 md:text-4xl text-2xl w-full px-3 !font-medium">
                    Latest Press Releases
                </Text>
                <hr className='border-1 mb-5 w-[98%] mx-auto' />

                <ul className="divide-y divide-gray-200 dark:divide-gray-700 px-3">
                    {!featureArticles.length && 'No posts found.'}
                    {featureArticles.map((post, id) => {
                        return (
                            <li key={id}
                                className="py-12">
                                <article>
                                    <div className="space-y-2 xl:grid xl:grid-cols-4 xl:items-baseline xl:space-y-0">
                                        <dl>
                                            <dt className="sr-only">Published on</dt>
                                            <dd className="text-base font-medium leading-6 text-gray-500 dark:text-gray-400">
                                                <time dateTime={post.date}>{post.date}</time>
                                            </dd>
                                        </dl>
                                        <div className="space-y-5 xl:col-span-3">
                                            <div className="space-y-6">
                                                <div className="flex flex-col gap-2 items-start">
                                                    <h2 className="text-xl md:text-2xl font-bold leading-8 tracking-tight text-gray-900 dark:text-gray-100 cursor-pointer hover:text-purple-500 dark:hover:text-purple-500"
                                                        onClick={() => setSelectedArtical(post)}
                                                    >
                                                        {post?.articleTitle}
                                                    </h2>
                                                    <div className="flex flex-wrap gap-2">
                                                        {post.tags.map((tag, i) => (
                                                            <span className="px-2.5 py-1 rounded-md shadow-md border-2 border-purple-600 text-sm md:text-md" key={i}>
                                                                {tag}
                                                            </span>
                                                        ))}
                                                    </div>
                                                </div>
                                                <div className="prose max-w-none text-gray-500 dark:text-gray-400">
                                                    {post.shortIntro.slice(0, 150)} ...
                                                </div>
                                            </div>
                                            <div className="text-base font-medium leading-6">
                                                {/* <LinkTo
                                                    external={true}
                                                    href={`https://pib.gov.in/PressReleasePage.aspx?PRID=1954574`}
                                                    className="text-primary-500 hover:text-primary-600 dark:hover:text-primary-400"
                                                    aria-label={`Read "${post.articleTitle}"`}
                                                >
                                                    Read more &rarr;
                                                </LinkTo> */}
                                                <button
                                                    onClick={() => {
                                                        setSelectedArtical(post)
                                                        // router.push('/script')
                                                    }} 
                                                    className="relative px-5 py-2 font-medium text-white group">
                                                    <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform translate-x-0 -skew-x-12 bg-purple-500 group-hover:bg-purple-700 group-hover:skew-x-12"></span>
                                                    <span className="absolute inset-0 w-full h-full transition-all duration-300 ease-out transform skew-x-12 bg-purple-700 group-hover:bg-purple-500 group-hover:-skew-x-12"></span>
                                                    <span className="absolute bottom-0 left-0 hidden w-10 h-20 transition-all duration-100 ease-out transform -translate-x-8 translate-y-10 bg-purple-600 -rotate-12"></span>
                                                    <span className="absolute bottom-0 right-0 hidden w-10 h-20 transition-all duration-100 ease-out transform translate-x-10 translate-y-8 bg-purple-400 -rotate-12"></span>
                                                    <span className="relative text-white text-xl">Make Script</span>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </article>
                            </li>
                        )
                    })}
                </ul>

                <Seperator />
            </>) : null
    )
}

export default FeaturedArticleSection