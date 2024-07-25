//
//  ContentView.swift
//  testAPIwithSwiftUI
//
//  Created by Théo Ajavon on 25/07/2024.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundStyle(.tint)
            Text("Hello, world!")
            Button {
                Task {
                    await makeRequests(route: "/")
                }
            } label: {
                Text("Make requests")
            }

        }
        .padding()
    }
}

#Preview {
    ContentView()
}
