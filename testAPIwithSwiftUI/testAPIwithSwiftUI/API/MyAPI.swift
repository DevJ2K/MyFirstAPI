//
//  MyAPI.swift
//  testAPIwithSwiftUI
//
//  Created by Théo Ajavon on 25/07/2024.
//

import Foundation

struct dataResponse: Codable {
    let response: Int
    let message: String
}

func makeRequests(route: String) async {
    let baseUrl = "http://127.0.0.1:2600"
    let urlString = baseUrl + route
    
    guard let url = URL(string: urlString) else {
        print("Unable to get this URL please try with an other one...")
        return
    }
    do {
        let (data, response) = try await URLSession.shared.data(from: url)
//        guard let response = response as? HTTPURLResponse
        
        let decodedResponse = try JSONDecoder().decode(dataResponse.self, from: data)
        print(decodedResponse)
        
    } catch {
        print("Failed to fetch data from API")
    }
}
