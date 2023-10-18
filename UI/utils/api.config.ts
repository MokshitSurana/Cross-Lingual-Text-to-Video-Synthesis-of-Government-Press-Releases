const ApiEndpoints = {
    baseUrl: process.env.NEXT_PUBLIC_BASE_URL
}

export const Api = {
    getScript: (): string => {
        return `${ApiEndpoints.baseUrl}/api/make_script`
    },
    getVideo: (): string => {
        return `${ApiEndpoints.baseUrl}/api/make_video`
    }
}