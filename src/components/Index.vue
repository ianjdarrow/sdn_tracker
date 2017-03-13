<template>
  <div class="container">
  <h1 v-if='loading'>Loading current SDN list</h1>
  <h1 v-if='error'>Error retrieving data</h1>
  <h1 v-else>SDN List Search</h1>
  <div class="input">
    <label>Enter a name:</label>
    <input type='text' v-model="search">
    <input type='checkbox' id='indCheckbox' v-model='showIndividuals'>
    <label for='indCheckbox'>Individuals</label>  
    <input type='checkbox' id='entityCheckbox' v-model='showEntities'>
    <label for='entityCheckbox'>Entities</label>
  </div>
  <div class="table" v-if='!loading && isInput'>
    <div id="ind-table" v-if='showIndividuals'>
      <h3>{{ filteredIndividuals.length }} individuals</h3>
      <table>
        <thead v-if='filteredIndividuals.length > 0'>
          <tr>
            <th class="ind-name">Name</th>
            <th>Details</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="individual in filteredIndividuals">
            <td>{{ individual.name }}</td>
            <td>{{ individual.details }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div id="entity-table" v-if='showEntities'>
      <h3>{{ filteredEntities.length }} entities</h3>
      <table>
        <thead v-if='filteredEntities.length > 0'>
          <tr>
            <th>Entity Name</th>
            <th>Affiliation</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entity in filteredEntities">
            <td>{{ entity.name }}</td>
            <td>{{ entity.details }}</td>
          </tr>
        </tbody>
      </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'index',
  data () {
    return {
      msg: 'LedgerX SDN Checker',
      individuals: [],
      entities: [],
      showIndividuals: true,
      showEntities: true,
      search: '',
      error: false,
      loading: true,
    }
  },
  methods: {
    getSDNIndividuals: function() {
      this.$http.get('http://127.0.0.1:5000/individuals').then(response => {
        this.individuals = response.body;
        }, response => {
          this.error = true;
        }
      );
    },
    getSDNEntities: function() {
      this.$http.get('http://127.0.0.1:5000/entities').then(response => {
        this.entities = response.body;
        this.loading = false;
        }, response => {
          this.error = true;
        }
      );
    }
  },
  computed: {
    filteredIndividuals: function() {
      return this.individuals.filter(individual => {
        return individual.name.indexOf(this.search.toUpperCase()) > -1
      });
    },
    filteredEntities: function() {
      return this.entities.filter(entity => {
        return entity.name.indexOf(this.search.toUpperCase()) > -1
      });
    },
    isInput: function() {
      return (this.search.length > 1);
    },
  },
  created: function() {
    this.getSDNIndividuals();
    this.getSDNEntities();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

th, td {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tr {
  height: 25px;
  vertical-align: top;
  line-height: 1.3em;
}

.ind-name {
  width: 30%;
}

.input {
  padding-bottom: 50px;
}

</style>
