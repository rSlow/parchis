import {useState} from "react";

export function useFetching(callback, globalError = false) {
    const [isLoading, setIsLoading] = useState(false)
    const [error, setError] = useState(null)

    async function fetching() {
        try {
            setIsLoading(true)
            const response = await callback()
            return response.data
        } catch (e) {
            setError(e.message)
        } finally {
            setIsLoading(false)
        }

    }

    return [fetching, isLoading, error]
}